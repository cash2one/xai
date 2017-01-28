

#calss header
class _HIGH():
	def __init__(self,): 
		self.name = "HIGH"
		self.definitions = [u'(especially of things that are not living) being a large distance from top to bottom or a long way above the ground, or having the stated distance from top to bottom: ', u'greater than the usual level or amount: ', u'containing a large quantity of something: ', u'very good or very moral standards: ', u'fast, strong wind: ', u'having power, an important position, or great influence: ', u'near or at the top of the range of sounds: ', u'(of food) smelling bad and no longer good to eat: ', u'not thinking or behaving normally because of taking drugs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
