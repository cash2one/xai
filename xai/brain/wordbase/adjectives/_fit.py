

#calss header
class _FIT():
	def __init__(self,): 
		self.name = "FIT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
