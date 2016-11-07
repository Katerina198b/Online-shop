from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

# Create your views here.
from product.models import Product
from likes.models import Likes
from django.http import JsonResponse
from likes.models import Dislikes
from product.models import Comment


def userLike(request, pk, obj):
    item_type = ContentType.objects.get_for_model(obj)
    like = Likes.objects.all().filter(user=request.user, item_types=item_type, item_id=pk)
    if like:
        like.delete()
        return True
    return False

def userDislike(request, pk, obj):
    item_type = ContentType.objects.get_for_model(obj)
    dislike = Dislikes.objects.all().filter(user=request.user, item_types=item_type, item_id=pk)
    if dislike:
        dislike.delete()
        return True
    return False

def productLike(request, pk):
    product = Product.objects.get(id=pk)
    if userLike(request, pk, Product):
        product.like = product.like - 1
    else:
        product.like = product.like + 1
        l = Likes()
        l.user = request.user
        l.item = product
        l.save()

    product.save()
    return JsonResponse({'like': product.like})


def productDislike(request, pk):
    product = Product.objects.get(id=pk)
    if userDislike(request, pk, Product):
        product.dislike = product.dislike - 1
    else:
        product.dislike = product.dislike + 1
        d = Dislikes()
        d.user = request.user
        d.item = product
        d.save()

    product.save()
    return JsonResponse({'dislike': product.dislike})


def commentLike(request, pk):
    comment = Comment.objects.get(id=pk)
    if userLike(request, pk, Comment):
        comment.like = comment.like - 1

    else:
        comment.like = comment.like + 1
        l = Likes()
        l.user = request.user
        l.item = comment
        l.save()

    comment.save()
    return JsonResponse({'like': comment.like})


def commentDislike(request, pk):
    comment = Comment.objects.get(id=pk)
    if userDislike(request, pk, Comment):
        comment.dislike = comment.dislike - 1

    else:
        comment.dislike = comment.dislike + 1
        d = Dislikes()
        d.user = request.user
        d.item = comment
        d.save()

    comment.save()
    return JsonResponse({'dislike': comment.dislike})

