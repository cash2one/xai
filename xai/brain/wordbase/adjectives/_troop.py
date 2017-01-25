

#calss header
class _TROOP():
	def __init__(self,): 
		self.name = "TROOP"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
