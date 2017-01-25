

#calss header
class _POSITIVE():
	def __init__(self,): 
		self.name = "POSITIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
