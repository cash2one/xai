

#calss header
class _ECLECTIC():
	def __init__(self,): 
		self.name = "ECLECTIC"
		self.definitions = [u'Methods, beliefs, ideas, etc. that are eclectic combine whatever seem the best or most useful things from many different areas or systems, rather than following a single system: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
