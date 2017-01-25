

#calss header
class _CHOICE():
	def __init__(self,): 
		self.name = "CHOICE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
