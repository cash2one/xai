

#calss header
class _FINANCIAL():
	def __init__(self,): 
		self.name = "FINANCIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
