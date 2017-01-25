

#calss header
class _NEXT():
	def __init__(self,): 
		self.name = "NEXT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
