

#calss header
class _VIDEO():
	def __init__(self,): 
		self.name = "VIDEO"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
