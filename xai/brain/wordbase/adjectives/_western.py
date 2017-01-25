

#calss header
class _WESTERN():
	def __init__(self,): 
		self.name = "WESTERN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
