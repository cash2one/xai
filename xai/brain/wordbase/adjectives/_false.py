

#calss header
class _FALSE():
	def __init__(self,): 
		self.name = "FALSE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
