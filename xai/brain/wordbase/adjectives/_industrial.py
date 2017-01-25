

#calss header
class _INDUSTRIAL():
	def __init__(self,): 
		self.name = "INDUSTRIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
