# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['파트타임 교육 과정','풀타임 교육 과정', '기타']
    })

@csrf_exempt
def message(request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        return_str = return_json_str['content']

        if  return_str == '파트타임 교육 과정':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 이어서 선택해주시기 바랍니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['과정1','과정2', '처음으로']
                }
            })
        elif  return_str == '과정1':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다아~. 이어서 선택해주시기 바랍니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['가격', '처음으로']
                }
        })

        elif return_str == '풀타임 교육 과정':
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
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n *반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!'
                }

            })
        elif return_str == 'iOS 개발 SCHOOL':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n *반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!'
                }

            })
        elif return_str == '웹 프로그래밍 SCHOOL':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n *반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!'
                }

            })
        elif return_str == '프론트엔드 개발 SCHOOL':
            return JsonResponse({

                'message': {
                    'text': return_str + '을 선택하셨습니다. 입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n *반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!'
                }

            })
        elif return_str == '처음으로':
            return JsonResponse({

                'message': {
                    'text': '처음부터 선택해주시기 바랍니다.'
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['파트타임 교육 과정','풀타임 교육 과정', '기타']
                }
            })
        elif return_str == '기타':
            return JsonResponse({

                'message': {
                    'text': '입력창 우측에 1:1 말풍선 버튼을 누른 후 말을 걸어주시면, 담당자를 빠르게 불러 드리겠습니다. \n *반드시 1:1 말풍선 버튼을 누른 후 말을 걸어주세요!'
                },
                'keyboard': {
                    'type': 'text'
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
