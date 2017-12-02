# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import models
# Create your views here.

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['실무 맞춤형 교육 (저녁/주말)','취업 연계 과정 (4개월 전일제)', '기타', '로또']
    })

@csrf_exempt
def message(request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        return_str = return_json_str['content']

        if  return_str == '실무 맞춤형 교육 (저녁/주말)':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 이어서 선택해주시기 바랍니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['미구현1','미구현2', '처음으로']
                }
            })

        elif return_str == '취업 연계 과정 (4개월 전일제)':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 이어서 선택해주시기 바랍니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['안드로이드 개발 SCHOOL','iOS 개발 SCHOOL', '웹 프로그래밍 SCHOOL', '프론트엔드 개발 SCHOOL', '기타', '처음으로']
                }
            })
        elif return_str == '안드로이드 개발 SCHOOL':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n\n *그냥 채팅창에 입력시 담당자 연결이 어려우니, 반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!*'
                }

            })

        elif return_str == 'iOS 개발 SCHOOL':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n\n *그냥 채팅창에 입력시 담당자 연결이 어려우니, 반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!*'
                }

            })
        elif return_str == '웹 프로그래밍 SCHOOL':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n\n *그냥 채팅창에 입력시 담당자 연결이 어려우니, 반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!*'
                }

            })
        elif return_str == '프론트엔드 개발 SCHOOL':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n\n *그냥 채팅창에 입력시 담당자 연결이 어려우니, 반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!*'
                }

            })
        elif return_str == '처음으로':
            return JsonResponse({

                'message': {
                    'text': '처음부터 선택해주시기 바랍니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['실무 맞춤형 교육 (저녁/주말)','취업 연계 과정 (4개월 전일제)', '기타']
                }
            })
        elif return_str == '기타':
            return JsonResponse({

                'message': {
                    'text': '입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n\n *그냥 채팅창에 입력시 담당자 연결이 어려우니, 반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!*'
                },
                'keyboard': {
                    'type': 'text'
                }     
            
            })
        elif return_str == '로또':
            return JsonResponse({

                'message': {
                    'text': models.lotto
                }

            })
        else:
         
            return JsonResponse({
                'message': {
                    'text': ''
                },

                'keyboard': {
                    'type': 'text'
                }     
            
            })
