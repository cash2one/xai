

#calss header
class _THEATRICAL():
	def __init__(self,): 
		self.name = "THEATRICAL"
		self.definitions = [u'belonging or relating to the theatre, or to the performance or writing of plays, opera, etc.: ', u'Theatrical behaviour is not sincere and too extreme and that is intended to attract attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
