from django.http import HttpResponse
from django.utils import simplejson as json
from django.utils.encoding import force_unicode

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        else:
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def json_response(dict_to_convert_to_json, has_date=False, translate_fields=[]):
    # fix for fields which use _('fasfasdf') to be translatable
    for field in translate_fields:
        dict_to_convert_to_json[field] = force_unicode(dict_to_convert_to_json[field])
    if has_date:
        return HttpResponse(json.dumps(dict_to_convert_to_json, cls=DateEncoder), mimetype="application/json")
    else:
        return HttpResponse(json.dumps(dict_to_convert_to_json), mimetype="application/json")    
