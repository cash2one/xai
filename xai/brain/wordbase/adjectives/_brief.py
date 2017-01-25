

#calss header
class _BRIEF():
	def __init__(self,): 
		self.name = "BRIEF"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
