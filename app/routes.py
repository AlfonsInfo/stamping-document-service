import os

from flask import request, jsonify, Blueprint
import uuid
main = Blueprint('main', __name__)
from app.model.dto import ReqStampingDto,ReqStampingDetailApproverDto
from engine import qrcode_engine, stamping_engine

@main.route("/sign-docs", methods=['POST'])
def sign_docs():
    # Get request data
    data = request.json
    # Mengurai data JSON menggunakan metode terpisah
    req_stamping_dto = parse_req_stamping_dto(data)
    app_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(app_dir, "output.pdf")
    # Generate a unique request ID
    req_id = str(uuid.uuid4())

    # Error handling for missing parameters
    if not all([req_stamping_dto.fileBase64, req_stamping_dto.documentId, output_path]):
        error_response = {
            "reqId": req_id,
            "status": 400,
            "message": "Missing required parameters",
            "error": "One or more required parameters are missing",
            "data": None
        }
        return jsonify(error_response), 400

    try:
        signature_base64 = qrcode_engine.generate_base64_qr(req_stamping_dto.documentId)
        # Call the doStamp function with appropriate parameters
        result = stamping_engine.do_stamp(
            data=req_stamping_dto,
            signature_base64=signature_base64,
            output_image_path=output_path
        )

        # Success response
        success_response = {
            "reqId": req_id,
            "status": 200,
            "message": "Document signed successfully",
            "error": None,
            "data": result   # Base 64 encoded signed document
        }
        return jsonify(success_response), 200
    except Exception as e:
        # Handle exceptions
        error_response = {
            "reqId": req_id,
            "status": 500,
            "message": "Internal server error",
            "error": str(e),
            "data": None
        }
        return jsonify(error_response), 500


def parse_req_stamping_dto(data):
    detail_approvers = [
        ReqStampingDetailApproverDto(**approver) for approver in data.get('detailApprover', [])
    ]

    req_stamping_dto = ReqStampingDto(
        title=data.get('title'),
        documentId=data.get('documentId'),
        status=data.get('status'),
        information=data.get('information'),
        detailApprover=detail_approvers,
        fileBase64=data.get('fileBase64')
    )

    return req_stamping_dto
