
import json
class _IS():
	def __init__(self):
		self.name = 'IS' 
		self.jsondata = {}
	#
	def run(self, obj1, obj2):
		# os.path.exists('_obj1.py')
		# try:
		# 	from xai.auto_classes import obj1
		# except:
		# 	class_creation(obj1)
		jsondata = {}
		jsondata[obj1[0]] = {}
		jsondata[obj2[-1]] = {}
		jsondata[obj1[0]]['parents'] = obj2
		jsondata[obj2[-1]]['childen'] = obj1

		return jsondata

# Run main function by default
if __name__ == "__main__":
    sent = 'banana is a long fruit'
    words = sent.split()
    print(words)
    index = words.index('is')
    print(index)
    obj1 = words[0:index]
    obj2 = words[index + 1:]
    print(obj1, '\n', obj2)
    _is = _IS()
    jsondata = _is.run(obj1, obj2)
    jsondata = json.dumps(jsondata, indent=4, sort_keys=True, separators=(',', ': '))
    print(jsondata)

