

#calss header
class _IMPORTANT():
	def __init__(self,): 
		self.name = "IMPORTANT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
