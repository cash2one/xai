

#calss header
class _GLIB():
	def __init__(self,): 
		self.name = "GLIB"
		self.definitions = [u'speaking or spoken in a confident way, but without careful thought or honesty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
