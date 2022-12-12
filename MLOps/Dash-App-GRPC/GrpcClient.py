# ***************************************************************** #
# (C) Copyright IBM Corporation 2022.                               #
#                                                                   #
# The source code for this program is not published or otherwise    #
# divested of its trade secrets, irrespective of what has been      #
# deposited with the U.S. Copyright Office.                         #
# ***************************************************************** #
import grpc
import os
from watson_nlp_runtime_client import (
    common_service_pb2,
    common_service_pb2_grpc,
    syntax_types_pb2,
)


class GrpcClient:

    NLP_MODEL_SERVICE_TYPE = os.getenv("NLP_MODEL_SERVICE_TYPE", default="mm-vmodel-id")

    # Default constructor
    def __init__(self):
        GRPC_SERVER_URL = os.getenv("GRPC_SERVER_URL", default="localhost:8085")
        print("###### Calling GRPC endpoint = ", GRPC_SERVER_URL)
        channel = grpc.insecure_channel(GRPC_SERVER_URL)
        self.stub = common_service_pb2_grpc.NlpServiceStub(channel)

    # A method calling syntax_izumo_en_stock model
    def call_syntax_izumo(self, inputText):
        request = common_service_pb2.SyntaxRequest(
            raw_document=syntax_types_pb2.RawDocument(text=inputText),
            parsers=syntax_types_pb2.SyntaxParserSpec(
                parsers=[syntax_types_pb2.SYNTAX_LEMMA]
            ),
        )
        SYNTAX_IZUMO_EN_STOCK_MODEL = os.getenv(
            "SYNTAX_IZUMO_EN_STOCK_MODEL", default="syntax-izumo-en-stock"
        )
        print("###### Calling remote GRPC model = ", SYNTAX_IZUMO_EN_STOCK_MODEL)
        response = self.stub.SyntaxIzumoPredict(
            request,
            metadata=[(self.NLP_MODEL_SERVICE_TYPE, SYNTAX_IZUMO_EN_STOCK_MODEL)],
        )
        return response

    # Tone analysis classification_ensemble-workflow_lang_en_tone-stock
    def call_tone_model(self, inputText):
        request = common_service_pb2.SentimentRequest(
            raw_document=syntax_types_pb2.RawDocument(text=inputText)
        )
        TONE_CLASSIFICATION_STOCK_MODEL = os.getenv(
            "TONE_CLASSIFICATION_STOCK_MODEL",
            default="classification_ensemble-workflow_lang_en_tone-stock",
        )
        print("###### Calling remote GRPC model = ", TONE_CLASSIFICATION_STOCK_MODEL)
        response = self.stub.ClassificationPredict(
            request,
            metadata=[(self.NLP_MODEL_SERVICE_TYPE, TONE_CLASSIFICATION_STOCK_MODEL)],
        )
        return response
