export PROJECT="learn-361304"
export LOCATION="us-central1"
gcloud run deploy genmedia-demos --source . --platform \
 managed --region $LOCATION --allow-unauthenticated --port 8501
