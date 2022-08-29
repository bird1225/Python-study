# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/29
import json
import requests
import datetime

pageUrl = "http://dev-server:8886/waveData/page"
dataUrl = "http://dev-server:8886/waveData/query"


def wave_page(page, page_size, tenant_id, collect_code, point_code, start, end):
    header = {'content-type': 'application/json'}
    data = {
        "tenantId": tenant_id,
        "collectCode": collect_code,
        "pointCode": point_code,
        "searchBeginTime": start,
        "searchEndTime": end,
        "pageNo": page,
        "pageSize": page_size
    }
    response = requests.post(url=pageUrl, data=json.dumps(data), headers=header)
    return json.loads(response.text)


def wave(tenant_id, collect_code, point_code, time):
    header = {'content-type': 'application/json'}
    data = {"time": time, "tenantId": tenant_id, "collectCode": collect_code,
            "pointCode": point_code}
    response = requests.post(url=dataUrl, data=json.dumps(data), headers=header)
    return json.loads(response.text)


if __name__ == '__main__':
    page = 1
    page_size = 20
    tenant_id = '00000001'
    collect_code = '202220136001'
    point_code = '1537366933664653313'
    start = '1659283200000'
    end = '1690819200000'
    page_data = wave_page(page, page_size, tenant_id, collect_code, point_code, start, end)
    rows = page_data.get('data').get('rows')
    row = rows[len(rows) - 1]
    timestamp = row.get('timeStamp')
    wave_data = wave(tenant_id, collect_code, point_code, timestamp)
    # print(wave_data.get('data').get('warmFormDatas'))
    print('租户:{}, 采集器:{}, 测点:{}, 时间:{} → {}'.format(tenant_id, collect_code, point_code, timestamp,
                                                    datetime.datetime.fromtimestamp(int(timestamp) / 1000).strftime(
                                                        "%Y-%m-%d %H:%M:%S")))
