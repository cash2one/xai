

#calss header
class _PRIVATE():
	def __init__(self,): 
		self.name = "PRIVATE"
		self.definitions = [u'only for one person or group and not for everyone: ', u'Private activities involve personal matters or relationships and are not related to your work: ', u'Private thoughts and opinions are secret and not discussed with other people: ', u'A private place is quiet and has no other people to see or hear you: ', u'A private person does not like to talk about their personal feelings and thoughts: ', u'If you talk to someone or do something in private, you do it without other people being present: ', u'controlled or paid for by a person or company and not by the government: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
