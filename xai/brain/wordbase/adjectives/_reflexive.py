

#calss header
class _REFLEXIVE():
	def __init__(self,): 
		self.name = "REFLEXIVE"
		self.definitions = [u'Reflexive words show that the person who does the action is also the person who is affected by it: ', u'done because of a physical reaction that you cannot control: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
