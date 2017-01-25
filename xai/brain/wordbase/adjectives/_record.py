

#calss header
class _RECORD():
	def __init__(self,): 
		self.name = "RECORD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
