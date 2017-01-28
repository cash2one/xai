

#calss header
class _SCHEMATIC():
	def __init__(self,): 
		self.name = "SCHEMATIC"
		self.definitions = [u'showing the main form and features of something, usually in the form of a drawing, in a way that helps people to understand it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
