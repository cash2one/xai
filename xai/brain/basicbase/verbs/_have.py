
import json
class _HAVE():
	def __init__(self):
		self.name = 'HAVE' 
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
		jsondata[obj1[0]]['childen'] = obj2
		jsondata[obj2[-1]]['parents'] = obj1

		return jsondata

# Run main function by default
if __name__ == "__main__":
    sent = 'banana have a yellow skin'
    words = sent.split()
    print(words)
    index = words.index('have')
    print(index)
    obj1 = words[0:index]
    obj2 = words[index + 1:]
    print(obj1, '\n', obj2)
    _have = _HAVE()
    jsondata = _have.run(obj1, obj2)
    jsondata = json.dumps(jsondata, indent=4, sort_keys=True, separators=(',', ': '))
    print(jsondata)

