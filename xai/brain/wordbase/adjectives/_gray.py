

#calss header
class _GRAY():
	def __init__(self,): 
		self.name = "GRAY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata