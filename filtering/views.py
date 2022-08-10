# from django.shortcuts import render, redirect
# from django.http import JsonResponse


# #머신러닝에 필요한 라이브러리
# # import sentencepiece

# from transformers import RobertaTokenizer, RobertaForSequenceClassification

# import torch
# from torch.nn import functional as F
# import traceback

# import os
# from queue import Queue, Empty
# from threading import Thread
# import time


# # 머신러닝 부분
# category_map = {
#     "0": "일반글",
#     "1": "공격발언",
#     "2": "차별발언"
# }

# category_map_logits = {
#     "0": "Default",
#     "1": "Offensive",
#     "2": "Hate"
# }

# #os.system('ls')

# tokenizer = RobertaTokenizer.from_pretrained('jason9693/SoongsilBERT-base-beep')
# model = RobertaForSequenceClassification.from_pretrained('jason9693/SoongsilBERT-base-beep')

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model.to(device)

# requests_queue = Queue()  # request queue.
# BATCH_SIZE = 100  # max request size.
# CHECK_INTERVAL = 0.11

# ##
# # Request handler.
# # GPU app can process only one request in one time.
# def handle_requests_by_batch():
#         while True:
#             request_batch = []
#             text_list = []

#             while not (len(request_batch) >= BATCH_SIZE):
#                 try:
#                     request = requests_queue.get(timeout=CHECK_INTERVAL)
#                     request_batch.append(request)
#                 except Empty:
#                     break

#             if len(request_batch) == 0:
#                 continue
#             # outputs = mk_predict(text_list)
#             valid_requests = []
#             valid_texts = []
#             for idx, request in enumerate(request_batch):
#                 types = request["input"][0]
#                 txt = request["input"][1]
#                 valid_texts.append(txt)
#                 valid_requests.append(request)
#             request_batch = []
#             # except Exception as e:
#             #     request["output"] = e
#             #     return

#             outputs = mk_predict(valid_texts)[0]
#             for idx, request in enumerate(valid_requests):
#                 try:
#                     dpstring = []
#                     output_item = outputs[idx]
#                     if request["input"][0] == "logits":
#                         return_item = {
#                             category_map_logits[str(k)]: v for k, v
#                             in enumerate(output_item.softmax(-1).tolist())}
#                     elif request["input"][0] == "dplogits":
#                         return_item = {
#                             category_map[str(k)]: v for k, v
#                             in enumerate(output_item.softmax(-1).tolist())}
#                     else:
#                         return_item = str(torch.argmax(output_item, -1).item())
#                         dpstring = category_map[return_item]

#                     if request["input"][0] == "dpclass":
#                         request["output"] = {0: category_map[return_item]}

#                     elif request["input"][0] == "dplogits":
#                         request["output"] = ({0: '<br>'.join(
#                             [f"{k}: {v:.4f}" for k, v in return_item.items()])}, 200)
#                     else:
#                         request["output"] = {
#                             "result": return_item,
#                             "dpstring": dpstring
#                         }
#                 except Exception as e:
#                     request["output"] = e
#         return


# handler = Thread(target=handle_requests_by_batch).start()



# ##
# # GPT-2 generator.
# def mk_predict(text_array: list):
#     try:
#         inputs = tokenizer(text_array, return_tensors="pt").to(device)
#         outputs = model(**inputs)[0]

#         return outputs, 200

#     except Exception as e:
#         traceback.print_exc()
#         return {'error': e}, 500


# # Get post request page.

# #@app.route('/filter/predict/<types>', methods=['POST'])
# def generate(request, types):
#     if request.method == 'POST':
#         # GPU app can process only one request in one time.
#         if types not in ['logits', 'class', 'dplogits', 'dpclass']:
#             return JsonResponse({'Error': 'Invalid types'}, status = 404)

#         # GPU app can process only one request in one time.
#         if requests_queue.qsize() > BATCH_SIZE:
#             return JsonResponse({'Error': 'Too Many Requests'}, status=429)

#         try:
#             args = []
#             text = request.POST['text']
#             args.append(types)
#             args.append(text)
#             print(args)

#         except Exception as e:
#             return JsonResponse({'message': 'Invalid request'}, status=500)

#         # input a request on queue
#         req = {'input': args}
#         requests_queue.put(req)

#         print(requests_queue)


#         # wait
#         while 'output' not in req:
#             time.sleep(CHECK_INTERVAL)

#         print(req)

#         return JsonResponse(req['output'])



