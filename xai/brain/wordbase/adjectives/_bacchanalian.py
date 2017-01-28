

#calss header
class _BACCHANALIAN():
	def __init__(self,): 
		self.name = "BACCHANALIAN"
		self.definitions = [u'(especially of a party) involving a lot of drinking of alcohol, uncontrolled behaviour, and possibly sexual activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
