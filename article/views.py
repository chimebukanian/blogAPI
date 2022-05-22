from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Articles
from .serializers import articleserializers
# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        articles=Articles.objects.all()
        serializer=articleserializers(articles, many=True)
        return Response({'article': serializer.data})
    
    def post(self, request):
        article=request.data.get('article')
        serializer=articleserializers(data=article)
        if serializer.is_valid(raise_execption=True):
            article_saved=serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved)})

    def put(self, request, pk):
        data=request.data.get('article')
        saved_article=get_object_or_404(Articles.objects.all(), pk=pk)
        serializer=articleserializers(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "Article '{}' updated sucessfully".format(saved_article)})

    def delete(self, request, pk):
        article_saved=get_object_or_404(Articles.objects.all(), pk=pk)
        article.saved.delete()
        return Response({"success":"Article '{}' deleted".format(article_saved)})