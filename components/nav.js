import Link from 'next/link'
import Head from 'next/head'

const links = [
  { href: '/about', label: 'About' },
  { href: '/faq', label: 'FAQ' }
]

export default function Nav() {
  return (
    <nav>
      <Head>
        <title>Stonks Dekho</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <ul className="flex justify-between items-center p-8">
        <li>
          <Link href="/">
            <a className="btn-blue no-underline">Home</a>
          </Link>
        </li>
        <ul className="flex justify-between items-center space-x-4">
          {links.map(({ href, label }) => (
            <li key={`${href}${label}`}>
              <Link href={href}>
                <a className="btn-blue no-underline">{label}</a>
              </Link>
            </li>
          ))}
        </ul>
      </ul>
    </nav>
  )
}
