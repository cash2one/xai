

#calss header
class _PROMPT():
	def __init__(self,): 
		self.name = "PROMPT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
