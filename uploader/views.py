import json
import boto3
from django.conf import settings
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse
from .models import UploadFile


class SignedURLView(generic.View):
    def post(self, request, *args, **kwargs):
        session = boto3.session.Session()
        client = session.client(
            "s3",
            region_name=settings.AWS_S3_REGION_NAME,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        url = client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": "media",
                "Key": f"uploads/{json.loads(request.body)['fileName']}",
            },
            ExpiresIn=300,
        )
        return JsonResponse({"url": url})


class UploadView(generic.CreateView):
    template_name = "upload.html"
    model = UploadFile
    fields = ['file']

    def get_success_url(self):
        return reverse("upload")

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context.update({
            "uploads": UploadFile.objects.all()
        })
        return context
