

#calss header
class _SQUARE():
	def __init__(self,): 
		self.name = "SQUARE"
		self.definitions = [u'having the shape of a square: ', u'used with units of measurement of length to express the total size of an area: ', u'Square is used immediately after measurements of length when expressing the length of the four sides of a square-shaped area: ', u'equal or level: ', u'If two people are all square, one of them has paid off a debt to the other and neither now owes or is owed any money.', u'If two teams or players are (all) square, they have an equal number of goals or points: ', u'in a straight line', u'used to describe a person who is boring and does not like new and exciting things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
