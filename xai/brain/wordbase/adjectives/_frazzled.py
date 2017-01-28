

#calss header
class _FRAZZLED():
	def __init__(self,): 
		self.name = "FRAZZLED"
		self.definitions = [u'extremely tired in a nervous or slightly worried way after a lot of mental or physical effort: ', u'burned or dried out after being in the sun or cooking for too long: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
