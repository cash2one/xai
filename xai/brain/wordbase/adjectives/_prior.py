

#calss header
class _PRIOR():
	def __init__(self,): 
		self.name = "PRIOR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
