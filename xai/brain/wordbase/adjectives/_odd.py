

#calss header
class _ODD():
	def __init__(self,): 
		self.name = "ODD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
