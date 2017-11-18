aws s3 sync . s3://hackforthesea.com --profile hackforthesea \
  --exclude ".git/*" \
  --exclude "deploy.sh" \
  --exclude ".idea/*" \
  --exclude ".gitignore"
