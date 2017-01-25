

#calss header
class _IMMEDIATE():
	def __init__(self,): 
		self.name = "IMMEDIATE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
