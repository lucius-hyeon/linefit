from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import Article
from .serializers import ArticleSerializer

class ArticleView(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
class ArticleDetailView(APIView):
    
    def get(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        if article.author == request.user:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg":"권한이 없습니다"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        if article.author == request.user:
            article.delete()
            return Response({"msg":"삭제 완료"}, status=status.HTTP_200_OK)
        return Response({"msg":"권한이 없습니다"}, status=status.HTTP_401_UNAUTHORIZED)
