

#calss header
class _CONTINUED():
	def __init__(self,): 
		self.name = "CONTINUED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
