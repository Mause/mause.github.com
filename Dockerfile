FROM jekyll/jekyll:latest
ENV JEKYLL_VERSION=3.8
LABEL Name=mause.github.com Version=0.0.1
EXPOSE 4000:4000
RUN apk add fish git git-perl vim