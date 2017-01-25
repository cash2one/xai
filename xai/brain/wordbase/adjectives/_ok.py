

#calss header
class _OK():
	def __init__(self,): 
		self.name = "OK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
