

#calss header
class _BAD():
	def __init__(self,): 
		self.name = "BAD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
