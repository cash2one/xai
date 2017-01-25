

#calss header
class _CANADIAN():
	def __init__(self,): 
		self.name = "CANADIAN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
