# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
import requests
from bs4 import BeautifulSoup as bs
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
                    'buttons': ['실무 맞춤형 교육 (저녁/주말)','취업 연계 과정 (4개월 전일제)', '기타', '로또']
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
            response = requests.get('http://www.nlotto.co.kr/gameResult.do?method=byWin')
            result = bs(response.text, 'html.parser')
            numbers = [tag['alt'] for tag in result.select('.contentsArticle p.number img')]
            count = result.find("h3",{"class":"result_title"}).text.split('\n')
            c1 = count[2]
            c2 = c1[1:-1]
            c3 = "제 {0} 회차 로또 당첨 번호는 {1}, {2}, {3}, {4}, {5}, {6} 이며, 2등 당첨 번호는 {7} 입니다.".format(count[0], numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6])

            return JsonResponse({

                'message': {
                    'text': c3
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
