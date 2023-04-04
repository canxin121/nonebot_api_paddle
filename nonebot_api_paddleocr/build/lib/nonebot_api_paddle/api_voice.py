import os
import requests
import json


def getvoice(text) -> str:
    url = 'https://aistudio.baidu.com/serving/app/10/run/predict/'

    headers = {
        'Content-Type': 'application/json',
        'Origin': 'https://aistudio.baidu.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'PSCBD=16%3A2_31%3A1; SE_LAUNCH=5%3A1680429424_16%3A28007298___31%3A28008975; __bsi=8248412395268301922_00_69_N_R_7_0303_cca8_Y; BA_HECTOR=ag808h2l8k048g80018halaj1i2lrmv1n; BAIDUID=E044455E10D5087EEC9D3C7B24F1A101:FG=1; H_WISE_SIDS=219946_234020_219563_216841_213348_214803_219943_213029_204916_230288_242157_110085_227870_236307_243890_244258_244715_240590_244955_245412_245701_246986_234207_248667_248725_243706_249910_249969_250145_247148_250738_251068_249344_247509_247461_251424_245919_251415_245217_252006_252221_247671_248079_250759_252562_249892_252577_252946_253044_252810_247585_252991_234296_253066_253463_253480_252354_253705_246823_250095_253516_253914_253427_229154_254217_254323_254458_254473_249983_254596_254261_254734_254683_248124_250226_251498_254749_254831_254890_249386_250390_251133_253900; H_WISE_SIDS_BFESS=219946_234020_114552_213347_214806_219943_213028_204904_230288_242157_242621_110085_227869_236307_243706_243887_244252_244722_240590_245412_246177_234208_247974_248725_249015_249633_247510_247148_250738_250889_251068_251127_245919_248239_247671_251415_251838_251884_252076_252262_250757_249893_247460_252580_252944_251150_253044_252811_247585_253170_234296_253064_248079_253480_252354_253704_246822_250091_251786_253976_253516_253914_253427_254143_229154_254296_254323_252306_254472_249981_179346_253900_254263_236539_254733_254683_248124_254687_254748_251132_244955_233835_8000072_8000124_8000137_8000149_8000161_8000163_8000166_8000171_8000193_8000204; BAIDUID_BFESS=72217B892980F06DF215AE904AC1B10F:FG=1; IMG_WH=428_804; PSTM=1679574152; BIDUPSID=135FA5FEB7755007A7A910CEA7AA5164'
    }

    data = {
        "fn_index": 0,
        "data": [text],
        "session_hash": "playgnwv9r"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    json_data = json.loads(response.text)
    file_name = str(json_data['data'][0]['name'])
    url = 'https://aistudio.baidu.com/serving/app/10/file=' + file_name
    downname = file_name.split("/")[-1]
    response = requests.get(url)
    with open(downname, "wb") as f:
        f.write(response.content)
    return url