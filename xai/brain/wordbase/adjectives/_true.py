

#calss header
class _TRUE():
	def __init__(self,): 
		self.name = "TRUE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
