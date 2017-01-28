

#calss header
class _HAPPY():
	def __init__(self,): 
		self.name = "HAPPY"
		self.definitions = [u'feeling, showing, or causing pleasure or satisfaction: ', u'(used in greetings for special occasions) full of enjoyment and pleasure: ', u'(of a condition or situation) lucky: ', u'(of words or behaviour) suitable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
