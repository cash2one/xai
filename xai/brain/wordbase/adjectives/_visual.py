

#calss header
class _VISUAL():
	def __init__(self,): 
		self.name = "VISUAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
